import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'lms.settings')
django.setup()

from books.models import Genre

# Create and save Genre objects
genre1 = Genre(name='Fiction')
genre1.save()

genre2 = Genre(name='Thriller')
genre2.save()

genre3 = Genre(name='Mystery')
genre3.save()

genre4 = Genre(name='Drama')
genre4.save()

genre5 = Genre(name='Action')
genre5.save()

genre6 = Genre(name='Romance')
genre6.save()

genre7 = Genre(name='Horror')
genre7.save()



    <!--Paypal payments-->

	<div id="paypal-button-container"></div>

	<script
		src="https://www.paypal.com/sdk/js?client-id=AaDbFCTAdi8NU4o-x6oOaBiLLoybkvO8w3xVZ2LgPAiTRwT4dDJu5u_ZecP9OtLTDvr7GZtZk_HuM3kq&currency=USD"></script>

	<script>

		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie !== '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = cookies[i].trim();
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) === (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}
		var csrftoken = getCookie('csrftoken');

		var total = '{{object.price}}'
		var productId = '{{object.id}}'

		function completeOrder() {
			var url = "{% url 'process_payment' %}"

			fetch(url, {
				method: 'POST',
				headers: {
					'content-type': 'application/json',
					'X-CSRFToken': csrftoken,
				},
				body: JSON.stringify({ 'productId': productId })
			})
		}



		// Render the PayPal button into #paypal-button-container
		paypal.Buttons({

			// Set up the transaction
			createOrder: function (data, actions) {
				return actions.order.create({
					purchase_units: [{
						amount: {
							value: total
						}
					}]
				});
			},

			// Finalize the transaction
			onApprove: function (data, actions) {
				return actions.order.capture().then(function (details) {
					// Show a success message to the buyer
					completeOrder()
					alert('Transaction completed by ' + details.payer.name.given_name + '!');
				});
			}


		}).render('#paypal-button-container');
	</script>
</div>
