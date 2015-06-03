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

	$('#toggle-event').change(function() {
		if ( myFlag == 0 ) 
		{
			$(".non-highlighted-pub").slideUp();
			$(".ocustom-smallheader").slideUp();
			/*
			$(".non-highlighted-pub").hide();
			$(".ocustom-smallheader").hide();
			*/
			myFlag = 1;
		} 
		else 
		{
			$(".ocustom-smallheader").show("slow");
			$(".non-highlighted-pub").show("slow");
			myFlag = 0;
		}
	})
}
