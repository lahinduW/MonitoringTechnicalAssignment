# Monitoring Technical Assignment

**Prerequisite:**

* Kubernetes cluster
* Helm, Kubectl, Docker and Git install server with access to Kubernetes cluster.



In this prometheus monitoring set up contains following commonents
1. Prometheus
2. Node expoter
3. Metrix server
4. Alertmanager
5. Grafana
6. Process counter exporter

## Architecture overview

![](https://monitoringdiagrams.s3.ap-southeast-1.amazonaws.com/prometheus_setup.png)

## Install

### Create custom process counter exporter docker image

**<GIT_HOME>** will refer to git clone directory

Navigate to <GIT_HOME>/CustomProcessCounterExporter directory

    $ docker build . -t <docker-repo-url>/process_counter_exporter:v1
    $ docker push <docker-repo-url>/process_counter_exporter:v1


### Setup monitoring 


Replace the process_counter_exporter docker image

    $ vi <GIT_HOME>/HelmCharts/process_counter_exporter/values.yaml

Change **image.repository** value

Update alertmanager email and slack config

    $ vi <GIT_HOME>/HelmCharts/alertmanager/alertmanager.yaml


### Setup monitoring

Deploy kube-state-metrics

    $ helm template kube-state-metrics <GIT_HOME>/HelmCharts/kube-state-metrics/
    $ helm install kube-state-metrics <GIT_HOME>HelmCharts/kube-state-metrics/

Deploy node-exporter 

    $ helm template node-exporter <GIT_HOME>/HelmCharts/node-exporter/
    $ helm install node-exporter <GIT_HOME>/HelmCharts/node-exporter/


Deploy process-counter-exporter 

    $ helm template process-counter-exporter <GIT_HOME>/HelmCharts/process-counter-exporter/
    $ helm install process-counter-exporter <GIT_HOME>/HelmCharts/process-counter-exporter/


Deploy alertmanager 
    
    $ helm template alertmanager <GIT_HOME>/HelmCharts/alertmanager/
    $ helm install alertmanager <GIT_HOME>/HelmCharts/alertmanager/


Deploy prometheus 

     $ helm template prometheus <GIT_HOME>/HelmCharts/prometheus/
     $ helm install prometheus <GIT_HOME>/HelmCharts/prometheus/


Deploy grafana 

    $ helm template grafana <GIT_HOME>/HelmCharts/grafana/
    $ helm install grafana <GIT_HOME>/HelmCharts/grafana/
    


