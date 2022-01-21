---
layout: post
title: "Helm Chart"
date: 2021-07-23 11:08:00 +0900
categories: [Kubernetes]
---

## Helm Chart

### 세가지 큰 개념

Chart는 Helm package이다. 이는 어플리케이션,tool, 또는 서비스를 쿠버네티스 클러스터에서 실행하기 위한 모든 리소스 정의들을 포함한다. 이를 쿠버네티스의 Hombrew formula라고 볼수 있다.

Repository는 chart가 수집되고 공유되는 장소이다. 이는 Perl의 CPAN archive와 유사하거나 Fedora Package Database와 유사하지만 쿠버네티스 패키지라는것이 차이다.

Release는 쿠버네티스 클러스터에서 실행중인 차트의 instance이다. 한개의 차트는 같은 클러스터에 여러번 설치될 수 있다. 설치될때마다, 새로운 release가 생성된다. MySQL 차트를 생각해보면, 클러스터에 2개의 데이터베이스가 실행중이라면, 차트를 두번 설치할 수 있다. 각각은 자신만의 release, release name이 있다.

이러한 개념을 가지고 Helm을 다음과 같이 설명할 수 있다.

> 헬름은 차트를 쿠버네티스에 설치하고, 각각의 installation에 대해서 새로운 release를 생성할 수 있다. 새로운 차트를 찾기 위해서, Helm chart repositories를 검색할 수 있다.

### Helm Dependency란?

[link](https://kb.novaordis.com/index.php/Helm_Dependencies)

- 장점 :chart의 templates 파일들을 다운받을 필요없이 values.yaml만 가지고 argoCD에 배포가능

## Commands

- 새로운 chart 생성 : `helm create [chart-name]`

- repo 추가 및 업데이트 : `helm repo add [repo-name] [repo-url]`

- Helm repo에 있는 특정 차트 검색 : `helm search repo bitnami | grep [chart name]`

- 특정 repo에 있는 helm chart download : `helm pull [repo]/[chart-name] --version [version]`

- Uninstall release : `helm uninstall [Release-name] [...] [flags]

- helm upgrade,install시 value orverride 예시 : `helm upgrade metric . --create-namespace -n metric --set password=***** --debug --install`
    - `--set` has a higher precedence than the default `values.yaml`



## Templating

- `{{ .Release.Name }}` injects the release name into the template.

- Add single quote : `{{ .Values.annotation | squote }}`

- [Built-in Objects](https://helm.sh/docs/chart_template_guide/builtin_objects/)

- Template Functions and Pipelines
    - `quote` : `{{ quote .Values.favorite.drink }}`, we can also use `squote`
    
    - [Go template language](https://godoc.org/text/template)
    
    - [Template Function List](https://helm.sh/docs/chart_template_guide/function_list/)
    
    - `print` : `print "Matt has " .Dogs " dogs"` , you can also use `println`
    
    - `printf` : `printf "%s has %d dogs." .Name .NumberDogs`
    
    - `time` : `trim` function removes white space from both sides of a string
    
      - `trim " hello "`: `hello`
    
    - `trimAll` 
    
      - `trimAll "$" "$5.00"` : `5.00` 
    
    - `trimPrefix`,`trimSuffix`
    
      
## Pipelines

- pipelines are a tool for chaining together a series of template commands to compactly express a series of transformations.
- eg 
  - `{{ .Values.favorite.drink | repeat 5 | quote }}`: `"coffeecoffeecoffeecoffeecoffee"`
  - `{{ .Values.favorite.food | upper | quote }}`: `"PIZZA"`

- `default` function

  - `default DEFAULT_VALUE GIVEN_VALUE`
  - `drink: {{ .Values.favorite.drink | default "tea" | quote }}`: if .Values.favorite.drink is specified, uses that value or uses `tea`
  - `default` command is perfect for computed values, which can not be declared inside `values.yaml`
    - `drink: {{ .Values.favorite.drink | default (printf "%s-tea" (include "fullname" .)) }}`

- `lookup` 

  - `lookup` function can be used to look up resources in a running cluster.

  - how to use : `lookup [apiVersion] [kind] [namespace] [name]`

    - `kubectl get pod mypod -n mynamespace` can be translated into `lookup "v1" "Pod" "mynamespace" "my pod"`

    - we can loop through multiple items in returned list.

      - ```go
        {{ range $index, $service := (lookup "v1" "Service" "mynamespace" "").items }}
            {{/* do something with each service */}}
        {{ end }}
        ```

      - keep in mind that Helm is not supposed to contact the Kubernetes API server during a `helm template` or `helm install | update | delete | rollback --dry-run`

- the operators (`eq`, `ne`, `lt`, `gt`, `and`, `or` and so on) are all implemented as functions. 



## Flow Control

- `with` can be used to modify scope

  - ``` yaml
      {{- with .Values.favorite }}
      drink: {{ .drink | default "tea" | quote }}
      food: {{ .food | upper | quote }}
      {{- end }}
    ```

    `with` statement sets `.` to point to `.Values.favorite`.

  - But inside of the restricted scope, you will not be able to access the other objects from the parent scope using `.`

  - If we want to access parent object, we can use like this.

    - ```yaml
        {{- with .Values.favorite }}
        drink: {{ .drink | default "tea" | quote }}
        food: {{ .food | upper | quote }}
        release: {{ $.Release.Name }}
        {{- end }}
      ```



## Variables

- ```yaml
    {{- $relname := .Release.Name -}}
    {{- with .Values.favorite }}
    drink: {{ .drink | default "tea" | quote }}
    food: {{ .food | upper | quote }}
    release: {{ $relname }}
    {{- end }}
  ```



## Named Templates

- naming convention

  - Most files in `templates/` are treated as if they contain Kubernetes manifests
  - `NOTES.txt` is one exception
  - files whose name begins with an underscore(_) are assumed to not have a manifest inside. These files are not rendered to Kubernetes object definition, but are available everywhere within other templates for use.

- `define` action allows us to create a named template inside of a template file.

  - ``` yaml
    {{- define "mychart.labels" }}
      labels:
        generator: helm
        date: {{ now | htmlDate }}
    {{- end }}
    ```

  - we can embed this template inside of our existing ConfigMap like this.

    - ```yaml
      apiVersion: v1
      kind: ConfigMap
      metadata:
        name: {{ .Release.Name }}-configmap
        {{- template "mychart.labels" }}
      data:
        myvalue: "Hello World"
        {{- range $key, $val := .Values.favorite }}
        {{ $key }}: {{ $val | quote }}
        {{- end }}
      ```

  - `define` functions should have a simple documentation block (`{{/* ... */}}`) describing what they do.

    - ```yaml
      {{/* Generate basic labels */}}
      {{- define "mychart.labels" }}
        labels:
          generator: helm
          date: {{ now | htmlDate }}
      {{- end }}
      ```

  - Since templates in subcharts are compiled together with top-level templates, it is best to name your templates with *chart specific names*. A popular naming convention is to prefix each defined template with the name of the chart: `{{ define "mychart.labels" }}`.

- To set scope for defined template, we should pass scope to template function parameter.

  - ```yaml
    {{/* Generate basic labels */}}
    {{- define "mychart.labels" }}
      labels:
        generator: helm
        date: {{ now | htmlDate }}
        chart: {{ .Chart.Name }}
        version: {{ .Chart.Version }}
    {{- end }}
    ```

  - to make above work, we should call template function like below.

    ```yaml
    {{- template "mychart.labels" . }}
    ```



## The `include` function

`template`function is action so, we can't pipline them. In this case, we can use `include` function.

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: {{ .Release.Name }}-configmap
  labels:
{{ include "mychart.app" . | indent 4 }}
data:
  myvalue: "Hello World"
  {{- range $key, $val := .Values.favorite }}
  {{ $key }}: {{ $val | quote }}
  {{- end }}
{{ include "mychart.app" . | indent 2 }}
```

so it is considered to use `include` over `template` in Helm templates simply so that the output formatting can be handled better for YAML documents.

