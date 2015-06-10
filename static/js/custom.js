function useQtips()
{
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
	// flag for toggling
	var myFlag = 0;
	var mySpeed = 500;

	$(".non-highlighted-pub").hide();

	$('#hide-show-pubs').click(function() {
		if ( myFlag == 0 ) 
		{
			// hide "selected" text
			$(".hide-on-click").hide();
			// show non-highlighted publications (i.e., all showing after click)
			$(".non-highlighted-pub").show("slow");
			$(".non-highlighted-pub").css('visibility','visible');
			// change text
			$('#hide-show-pubs').html("<b>SHOW SELECTED PUBLICATIONS</b>")
			// toggle flag
			myFlag = 1;
		} 
		else 
		{
			// slow "selected" text
			$(".hide-on-click").show("slow");
			// hide non-highlighted publications
			$(".non-highlighted-pub").slideUp();
			$(".non-highlighted-pub").css('visibility','hidden');
			// change text
			$('#hide-show-pubs').html("<b>SHOW ALL PUBLICATIONS</b>")
			// toggle flag
			myFlag = 0;
		}
	})
}
