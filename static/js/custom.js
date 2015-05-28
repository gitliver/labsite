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
