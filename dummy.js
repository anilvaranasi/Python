(function process( /*RESTAPIRequest*/ request, /*RESTAPIResponse*/ response) {

    // implement resource here
    var sLog = '';
    var pathParams = request.pathParams;
    var operation = pathParams.operation; //'myApp_table' 
    var issueId = pathParams.id; //'1234'

    sLog += "\n operation=" + operation;
    sLog += " \n id=" + issueId;
    var issueDetails = '';
    issueDetails = getIssueDetails(issueId);
    //sLog += '\n IssueDetails=' + issueDetails;
    var issueJson = JSON.parse(issueDetails);
    var issueSummary = issueJson.fields.summary;
    //var issueDesc = issueJson.fields.description;
    var issueDesc = issueJson.fields.description.content[0].content[0].text;
    //var issueDescString = JSON.stringify(issueDesc);
    sLog += "\n Issue id = " + issueJson.id;
    sLog += "\n Issue description = " + issueDesc;
    sLog += "\n issueSummary = " + issueSummary;

    gs.log(sLog, 'jiraint');
    //Get Issue details from Jira and create an incident in ServiceNow
    if (operation.indexOf('JiraIssueCreation') > -1) {
        createIncident(issueId, issueSummary, issueDesc);
    }

    function createIncident(issueId, issueSummary, issueDesc) {
        var grInc = new GlideRecord('incident');
        grInc.initialize();
        grInc.short_description = issueSummary;
        grInc.description = issueDesc;
        grInc.correlation_id = issueId;
        grInc.correlation_display = 'jira';
        grInc.insert();
    }

    function getIssueDetails(issueID) {
        try {
            var r = new sn_ws.RESTMessageV2('JiraIntegration', 'Get Issue Details');
            // r.setStringParameterNoEscape('issueID', 'SE-23');
            r.setStringParameterNoEscape('issueID', issueID);

            //override authentication profile 
            //authentication type ='basic'/ 'oauth2'
            //r.setAuthenticationProfile(authentication type, profile name);

            //set a MID server name if one wants to run the message on MID
            //r.setMIDServer('MY_MID_SERVER');

            //if the message is configured to communicate through ECC queue, either
            //by setting a MID server or calling executeAsync, one needs to set skip_sensor
            //to true. Otherwise, one may get an intermittent error that the response body is null
            //r.setEccParameter('skip_sensor', true);

            var response = r.execute();
            var responseBody = response.getBody();
            var httpStatus = response.getStatusCode();
        } catch (ex) {
            var message = ex.message;
        }
        return responseBody;
        //return JSON.stringify(request.body.data) ; //gs.log(JSON.stringify(request.body.data));
    }


})(request, response);