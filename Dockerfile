FROM newtmitch/sonar-scanner AS sonarqube_scan
WORKDIR /
COPY . .
RUN ls -list
# sonar.projectName property used for providing human-friendly project name in addition 
# for projectKey
RUN sonar-scanner \
    -Dsonar.host.url="http://localhost:9000" \
    -Dsonar.login="5514336c208f72bed1976ff63656df9d9de1ebf1" \
    -Dsonar.projectKey="QAV1" \
    -Dsonar.sources="." \
    -Dsonar.projectName="QAV1"
