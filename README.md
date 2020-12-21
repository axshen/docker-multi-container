# quick-K8s

Useful repository for prototyping and deploying a simple web application with Kubernetes. Use docker-compose/Minikube for running locally and DigitalOcean for production deployment. 

The sample application produces the value of the nth Fibonacci sequence number (recursively), where n is provided as an argument. The time to compute each value is also calculated. It is very slow to calculate numbers in the Fibonacci sequence recursively (lots of redundant calculations) so as the argument provided gets larger, the longer it will take to compute.

The Redis cache stores the arguments and values. We also allow the user to compute the Fibonacci value accessing the cache where possible. It is interesting to see the speed up that this produces for large n. This example is used because the architecture consists of a connected API, user interface and database, which is pretty common for web projects. Replace the images as necessary.

## Docker compose

The quickest way to get this sample application up is with [docker-compose](https://docs.docker.com/compose/). This is useful for development. To do this:

1. `docker build -t api api` (build API image)
2. `docker build -t ui ui` (build UI image)
3. `docker-compose up` (run containers together)

## Minikube

TBA

## DigitalOcean

TBA

To create a Kubernetes ingress on Digital Ocean:

* `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v0.40.2/deploy/static/provider/do/deploy.yaml`

Some useful links:

* [CICD tutorial](https://www.digitalocean.com/community/tutorials/how-to-automate-deployments-to-digitalocean-kubernetes-with-circleci)
* To set up the ingress: [ingress tutorial](https://www.digitalocean.com/community/tutorials/how-to-set-up-an-nginx-ingress-with-cert-manager-on-digitalocean-kubernetes#step-2-%E2%80%94-setting-up-the-kubernetes-nginx-ingress-controller)
