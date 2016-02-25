function setUp() {

    /* This function hides some tags in the html doc; binds the submit gene 
     * function to the button; */

    // hide these to begin with
    $(".startHidden").hide();
    $(".notFoundAlert").hide();

    // activate autocomplete
    autoComp();

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

function submitData() {

    // This function queries the db with an AJAX call when the user submits a gene
    // ( sanitize input? )

    // the URL from which to GET
    myUrl = '/_get_albert_data';

    // JSON to submit to server
    var data_in = { mygene: $('input[name="geneInput"]').val() };

    // console.log(data_in);

    // get data from server
    // docs: // jQuery.getJSON( url [, data ] [, success ] )
    $.getJSON(myUrl, data_in, function(data) {
        
        // console.log(data);

        if (data.img == 'notfound') {
            // show alert
            $(".notFoundAlert").show();
            $(".startHidden").hide();
        } else {
            // show the fields
            $(".startHidden").show();
            $(".notFoundAlert").hide();

            // insert the images into HTML tags
            $("#insertImg").html('<img src="' + data.img + '" alt="image" width="800">');
        }
    });

    return false;
}

function autoComp() {

    // This function makes autocomplete active 

    // the URL from which to GET
    myUrl = '/_autocomplete';

    $.ajax({
        url: myUrl
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

setUp();
