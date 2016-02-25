function useQtips()
{
    // add qTip speech bubbles to big circle categories (Publications, People, Research) on the homepage

    // Grab all elements with the class "hasTooltip"
    $('.hasTooltip').each(function() {
        // console.log('Testing')
        // console.log($(this).next('div').html())
        $(this).qtip({
        style: { 
                // classes: 'qtip-light',
                classes: 'qtip-bootstrap',
            tip: { corner: 'left center' }
                },
            position: {
            // target: 'mouse'
            my: 'top left',  // Position my top left...
                at: 'top right', // at the bottom right of...
            target: $(this) // my target
        },
        content: {
            text: $(this).next('div').html() // Use the "div" element next to this for the content
        }
        });
    });
}

function highlightSelected()
{
    // Change the view on Publications page to show/hide selected publications

    // flag for toggling
    var myFlag = 1;
    var mySpeed = 500;

    /* 
    using this overkill (hide + the visibility property) to prevent 
    the hidden element from flashing quickly on page load
    */
    $(".show-on-click").hide();
    $(".show-on-click").css('visibility','visible');

    $('#hide-show-pubs').click(function() {
        if ( myFlag == 0 ) 
        {
            // hide "selected" text
            $(".show-on-click").hide();
            // show non-highlighted publications (i.e., all showing after click)
            $(".non-highlighted-pub").show("slow");
            $(".non-highlighted-pub").css('visibility','visible');
            // change text
            $('#hide-show-pubs').html("<b>SHOW SELECTED PUBLICATIONS</b>");
            // toggle flag
            myFlag = 1;
        } 
        else 
        {
            // show "selected" text
            $(".show-on-click").show("slow");
            // hide non-highlighted publications
            $(".non-highlighted-pub").slideUp();
            $(".non-highlighted-pub").css('visibility','hidden');
            // change text
            $('#hide-show-pubs').html("<b>SHOW ALL PUBLICATIONS</b>");
            // toggle flag
            myFlag = 0;
        }
    })
}
