var toastTrigger = document.querySelector(".messages");
var toastLiveExample = document.getElementById("liveToast");
if (toastTrigger) {
  var toast = new bootstrap.Toast(toastLiveExample);

  toast.show();
}
