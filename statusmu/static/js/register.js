$("#email").keyup(() => {
  const rgx = /^\w+([\\.-]?\w+)*@\w+([\\.-]?\w+)*(\.\w{2,3})+$/;
  const value = $("#email").val();
  console.log(rgx.test(value));
});
