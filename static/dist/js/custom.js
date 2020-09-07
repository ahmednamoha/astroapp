$('input[name$="file"]').addClass("custom-file-input");

if ($("div.error").length > 0) {
  $('input[name$="exten"]').addClass("is-invalid");
  $(document).Toasts("create", {
    class: "bg-danger",
    title: "short Code",
    subtitle: "Erro",
    body: "Fadlan Diwaangali  midkale Kan horay ayuu ujiray",
  });
} else {
  alert(" maya lamhelin ");
}
