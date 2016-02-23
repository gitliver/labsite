function monitorJobs() {

    /* This function SGE monitors jobs and returns the output when it comes into being */

    console.log('Testing...');

    // the URL from which to GET
    myUrl = '/universaltaxdist/qstat/';
    myUrl2 = '/universaltaxdist/files/';

    // data input
    var data_in = null;

    // job id
    var job_id = $('#jobid').text();
    // console.log(job_id);

    // query api at intervals
    var timer = setInterval(function(){
        console.log(myUrl);
        // get data from server
        // docs: jQuery.getJSON( url [, data ] [, success ] )
        $.getJSON(myUrl + job_id, data_in, function(data) {
            // insert info into HTML tags
            console.log(data);
            console.log(data.state);
            $('#jobstatus').html(data.state);
	    // break loop if job finishes
	    if (data.state == '') {
                clearInterval(timer);
                $('#jobstatus').html('Your job has finished!');

                $.getJSON(myUrl2 + job_id, data_in, function(data2) {
                    if (data2.files == '1') {
                        // insert the images into HTML tags
                        $("#insertImg1").html('<img src="/static/img/uploads_img/KL_plot' + job_id  + '.png" alt="image" width="800">')
                        $("#insertImg2").html('<img src="/static/img/uploads_img/loglin_plot' + job_id  + '.png" alt="image" width="800">')
                        $("#insertImg3").html('<img src="/static/img/uploads_img/loglog_plot' + job_id  + '.png" alt="image" width="800">')
                    }
                    else {
                        console.log('Your job has failed');
                    }
                }); // files created?
            } // qstat == ''
        }); // job state 
    }, 5000); // timer
}

monitorJobs();
