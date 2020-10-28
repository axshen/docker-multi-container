# quick-K8s

Code for a quick deployment of a basic web application using Kubernetes. Uses DigitalOcean for cloud resources and Travis CI for CI/CD. Contains custom client, server and async worker code. 

Also contains a docker-compose file for running locally.

To create a Kubernetes ingress on Digital Ocean:

* `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.40.2/deploy/static/provider/do/deploy.yaml`

Some useful links:

* [CICD tutorial](https://www.digitalocean.com/community/tutorials/how-to-automate-deployments-to-digitalocean-kubernetes-with-circleci)
* To set up the ingress: [ingress tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nginx-ingress-with-cert-manager-on-digitalocean-kubernetes#step-2-%E2%80%94-setting-up-the-kubernetes-nginx-ingress-controller)