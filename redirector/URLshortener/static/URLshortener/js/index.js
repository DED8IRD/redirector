$(function(){
	// Show modal
	$('#url-modal').modal('show')

	$('.copy-button').each((idx, obj) => {
		// Initialize the tooltips.
		$(obj).tooltip()
		// Handler for updating the tooltip message.
		$(obj).bind('copied', function(event, message) {
			$(this).attr('data-original-title', message)
					.tooltip('show')
		})
		// When the copy button is clicked, select the value of the text box, attempt
		// to execute the copy command, and trigger event to update tooltip message
		// to indicate whether the text was successfully copied.
		$(obj).bind('click', function() {
			let input = $(obj).closest('.input-group').find('.copy-input')
			input.select()
			console.log(input)
			try {
				let success = document.execCommand('copy')

				if (success) {
					$(obj).trigger('copied', ['Copied!'])
				} else {
					$(obj).trigger('copied', ['Copy with Ctrl-C'])
				}
			} catch (err) {
				$(obj).trigger('copied', ['Copy with Ctrl-C'])
			}
		})
	})
})

