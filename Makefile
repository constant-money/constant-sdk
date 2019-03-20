deploy:
	rm deployments.tar.enc;
	tar cvf deployments.tar deployments/;
	travis encrypt-file deployments.tar;
	rm deployments.tar;