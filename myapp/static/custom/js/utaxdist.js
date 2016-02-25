function monitorJobs() {

    /* This function SGE monitors jobs and returns the output when it comes into being */

    /* console.log('Testing...'); */

    // the api URLs from which to GET
    // qstat status
    myUrl = '/universaltaxdist/qstat/';
    // file status
    myUrl2 = '/universaltaxdist/files/';

    // data input
    var data_in = null;

    // job id
    var job_id = $('#jobid').text();
    // console.log(job_id);

    // job state
    var jobstate = '';

    // translate qstat state into human readable
    var jobstatetable = {
        'r': 'running',
        'qw': 'queued',
        'Eqw': 'error',
    };

    // coarse implementation of a spinning wheel
    var counter = 8;
    var jobwheel = {
        0: '|',
        1: '/',
        2: '-',
        3: '\\',
        4: '|',
        5: '/',
        6: '-',
        7: '\\',
        8: '|',
    };

    // dots to print while waiting for queued job
    var dots = '';

    // query api at intervals
    var timer = setInterval(function(){
        // console.log(myUrl);
        // get data from server
        // docs: jQuery.getJSON( url [, data ] [, success ] )
        $.getJSON(myUrl + job_id, data_in, function(data) {

	    // if job state well defined
            if (data.state in jobstatetable) {
                jobstate = jobstatetable[data.state];
		dots += '.';
                // counter++; 
            }
            else {
                jobstate = data.state;
            }

            // insert info into HTML tags
            $('#jobstatus').html(jobstate);
            // $('#jobwheel').html(jobwheel[counter % 9]);
            $('#jobwheel').html(dots);

	    // break loop if job finishes
	    if (data.state == '') {
                clearInterval(timer);
                $('#jobstatus').html('Your job has finished!');
                $('#jobwheel').html('');

                $.getJSON(myUrl2 + job_id, data_in, function(data2) {
                    if (data2.files == '1') {
                        // insert the images into HTML tags
                        $("#insertImg1").html('<img src="/static/img/uploads_img/KL_plot' + job_id  + '.png" alt="image" width="800">')
                        $("#insertImg2").html('<img src="/static/img/uploads_img/loglin_plot' + job_id  + '.png" alt="image" width="800">')
                        $("#insertImg3").html('<img src="/static/img/uploads_img/loglog_plot' + job_id  + '.png" alt="image" width="800">')
                    }
                    else {
                        $('#jobstatus').html('Your job has failed');
                    }
                }); // files created?
            } // qstat == ''
        }); // job state 
    }, 5000); // timer
}

monitorJobs();
