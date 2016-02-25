function addQTips() {

    /* This function enables qtips, which explain the fields 
     * which pop up after the user submits a gene, then mouses
     * over a property */

    // html IDs to be written into
    var myIdArray = ["idgene",
            "idcell",
            "idmean",
            "idmin",
            "idmax",
            "idconn",
            "idpval",
            "idqval",
            "idcent",
            "iddisp",
            "idrna",
            "idsplice",
            "idsurf",
            "idreg"];

    // explanation of each field
    var myTextArray = [ "The gene",
              "The number of cells where expression of the gene is detected",
              "Mean expression value in log_2(1+TPM) scale",
              "Min expression value in log_2(1+TPM) scale",
              "Max expression value in log_2(1+TPM) scale",
              'Connectivity quantifies how "connected" the expression of the gene appears in the topological graph',
              "Statistical significance of the connectivity. Highly significant genes are specific to particular cell populations or stages",
              "Statistical significance (FDR) of connectivity after Benjamini-Hochberg adjustment for multiple testing",
              "Position (in number of edges units) of the gene expression centroid with respect to the inferred root node (the most stem-like node). High (low) values correspond to genes expressed in post-mitotic (totipotent) cells",
              "Dispersion of the centroid (in number of edges units)",
              "Whether the gene belongs to gene ontology GO0044822, poly(A) RNA binding",
              "Whether the gene belongs to gene ontology GO0008380, RNA splicing",
              "Whether the protein encoded by the gene has an extracellular domain, according to InterPro database",
              "Whether the gene belongs to gene ontology GO0006355, Regulation of transcription, DNA-templated" ];

    // add qtips to fields
    for (var i = 0; i < myIdArray.length; i++) {
        $("#" + myIdArray[i]).qtip({
        content: myTextArray[i],
        style: {classes: 'qtip-rounded qtip-bootstrap'}, 
        });
    }

}

function bindSubmit() {

    /* This function binds the submit gene function to the submit button */

    // bind submitData() function to either clicking 'submit' button OR pressing enter
    // http://stackoverflow.com/questions/1384037/binding-an-existing-javascript-function-in-jquery
    $('a#getInput').bind("click", submitData);

    // if press enter
    $('input').keypress(function (e) {
        var key = e.which;
        if (key == 13)  // the enter key code
        {
            submitData();
        }
    });  

}

function getDb() {

    // determine which database table the user queries when he enters the gene

    var whichdb = "db1";

    // if db2 radio button is checked, switch db
    if ($('#db2').is(":checked")) {
        whichdb = "db2";
    }

    return whichdb;
}

function submitData() {

    // This function queries the db with an AJAX call when the user submits a gene
    // ( sanitize input? )

    // the URL from which to GET
    myUrl = '/_get_gene_result';

    // choose db
    var whichdb = getDb();

    // JSON to submit to server
    var data_in = { mygene: $('input[name="geneInput"]').val(),
            mydb: whichdb };

    // get data from server
    // docs: // jQuery.getJSON( url [, data ] [, success ] )
    // Description: Load JSON-encoded data from the server using a GET HTTP request.
    // url (Type: String) - A string containing the URL to which the request is sent.
    // data (Type: PlainObject or String) -  A plain object or string that is sent to the server with the request.
    // success (Type: Function( PlainObject data, String textStatus, jqXHR jqXHR ) ) - A callback function that is executed if the request succeeds.
    $.getJSON(myUrl, data_in, function(data) {
        
        // console.log(data);

        if (data.Gene == 'not found') {
            // show alert
            $(".notFoundAlert").show();
            $(".startHidden").hide();
        } else {
            // show the fields
            $(".startHidden").show();
            $(".notFoundAlert").hide();

            // insert the data from the database into HTML tags
            $("#idgene").html('Gene: <b>' + data.Gene + '</b>')
            $("#idcell").html('Cells <b>' + data.Cells + '</b>')
            $("#idmean").html('Mean: <b>' + data.Mean + '</b>')
            $("#idmin").html('Min: <b>' + data.Min + '</b>')
            $("#idmax").html('Max: <b>' + data.Max + '</b>')
            $("#idconn").html('Connectivity: <b>' + data.Connectivity + '</b>')
            $("#idpval").html('<i>p</i>-value: <b>' + data.p_value + '</b>')
            $("#idqval").html('<i>q</i>-value (BH): <b>' + data.BH_p_value + '</b>')
            $("#idcent").html('Centroid: <b>' + data.Centroid + '</b>')
            $("#iddisp").html('Dispersion: <b>' + data.Dispersion + '</b>')
            $("#idrna").html('RNA binding: <b>' + data.RNA_binding + '</b>')
            $("#idsplice").html('Splicing Factor: <b>' + data.Splicing + '</b>')
            $("#idsurf").html('Surface Marker: <b>' + data.Surface + '</b>')
            $("#idreg").html('Regulation of Transcription: <b>' + data.Transcription + '</b>')
            // insert the images into HTML tags
            $("#insertKey").html('<div style="margin-left: 70px;"><br><small>' + parseFloat(data.Max).toPrecision(3) + '</small><br><img style="margin-left: -5px;" src="/static/img/other/scale.80.330.jpg" alt="image" height="220" width="35"><br><small>' + parseFloat(data.Min).toPrecision(3) + '</small></div>')
            $("#insertImg1").html('<img src="' + data.img1 + '" alt="image" width="400">')
            $("#insertImg2").html('<div style="margin-left: 50px;">Zoom of progenitor region:</div><img src="' + data.img2 + '" alt="image" width="400">')
            $("#insertImg3").html('<div style="margin-left: 50px;">Zoom of post-mitotic region:</div><img src="' + data.img3 + '" alt="image" width="400">')
            $("#insertImg4").html('<div style="margin-left: 50px;">Reconstructed expression timeline:</div>' + '<img src="' + data.img4 + '" alt="image" width="800">' + '<div style="text-align: center;"><small>day</small></div>')
        }
    });

    return false;
}

function motorAutoComp() {

    // This function makes autocomplete active 

    // the URL from which to GET
    myUrl = '/_motor_autocomplete';

    // choose db
    var whichdb = getDb();

    $.ajax({
        url: myUrl,
        dataType: "json",
        data: {
            mydb: whichdb
        }
    }).done(function (data) {
        $('input[name="geneInput"]').autocomplete({
            source: data.json_list,
            minLength: 2
        });
    });

}

// http://blog.miroslavpopovic.com/2012/06/23/jqueryui-autocomplete-filter-words-starting-with-term/
// Overrides the default autocomplete filter function to 
// search only from the beginning of the string
$.ui.autocomplete.filter = function (array, term) {
    var matcher = new RegExp("^" + $.ui.autocomplete.escapeRegex(term), "i");
    return $.grep(array, function (value) {
        return matcher.test(value.label || value.value || value);
    });
};

console.log('Testing123');

// hide these to begin with
$(".startHidden").hide();
$(".notFoundAlert").hide();

// add qTips
addQTips();
// enable autocomplete
motorAutoComp();
// bind submit function to submit button
bindSubmit();

// every time the radio button is clicked,
// the autocomplete function is called to
// provide entries from the chosen database
$("input:radio").click(function() {
    // alert("clicked");
    motorAutoComp();
});
