document.addEventListener('DOMContentLoaded', function() {
    const buyNowButton = document.getElementById('buy-now-button');

    buyNowButton.addEventListener('click', function() {
        // Redirect to the buy now page or perform the desired action
        window.location.href = paymentUrl;

    });
});

document.getElementById('payment-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const amount = document.getElementById('amount').value;
    // You can redirect to a payment gateway or perform any desired action here
    // For this example, we'll simulate a redirect using setTimeout
    setTimeout(() => {
        window.location.href = 'success.html'; // Redirect to success page
    }, 2000); // Simulate delay
});