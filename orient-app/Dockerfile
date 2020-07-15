FROM java:8  
VOLUME /tmp   
ADD orient-app/orient-app-1.0.0-SNAPSHOT.jar /app.jar
ENTRYPOINT ["java","-Djava.security.egd=file:/dev/./urandom","-jar","/app.jar"]
