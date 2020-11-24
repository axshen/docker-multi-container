# quick-K8s

Code for quickly deploying a simple web application with Kubernetes. I am using DigitalOcean for cloud resources. This app is comprised of a frontend, backend and database (all containerised). For local development we include a docker-compose file.

To create a Kubernetes ingress on Digital Ocean:

* `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.40.2/deploy/static/provider/do/deploy.yaml`

Some useful links:

* [CICD tutorial](https://www.digitalocean.com/community/tutorials/how-to-automate-deployments-to-digitalocean-kubernetes-with-circleci)
* To set up the ingress: [ingress tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nginx-ingress-with-cert-manager-on-digitalocean-kubernetes#step-2-%E2%80%94-setting-up-the-kubernetes-nginx-ingress-controller)
