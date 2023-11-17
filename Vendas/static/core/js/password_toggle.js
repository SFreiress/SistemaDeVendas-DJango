$(document).ready(function () {
  $('#togglePassword').click(function () {
    var passwordField = $('#passwordInput');
    var icon = $('#toggleIcon');

    if (passwordField.attr('type') === 'password') {
      passwordField.attr('type', 'text');
      icon.removeClass('fa-eye-slash').addClass('fa-eye');
    } else {
      passwordField.attr('type', 'password');
      icon.removeClass('fa-eye').addClass('fa-eye-slash');
    }
  });
});