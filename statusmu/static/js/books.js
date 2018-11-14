$(document).ready(() => {
  $.ajax({
    url: "/api/books/",
    success: result => {
      const books = localStorage.getItem("books");
      const data = JSON.parse(books);
      const idItems = {};
      result.data.map((item, index) => {
        if (!books) idItems[item.id] = false;
        $("#items").append(
          `<tr id=${item.id}>
            <td>${index + 1}</td>
            <td><img src=${item.image}></td>
            <td>
              <ul>
                <li>
                  <b>Title</b> : ${item.title}
                </li>
                <li>
                  <b>Author</b> : ${item.author}
                </li>
                <li>
                  <b>Description</b> : ${
                    item.desc.length < 300 ? item.desc : item.desc + "..."
                  }
                  <a href=${item.preview}>More</a>
                </li>
              </ul>
            </td>
            <td>
              <i class='${
                !!books && data[item.id] ? "fas" : "far"
              } fa-star' onclick='fav("${item.id}")'></i>
            </td>
          </tr>`
        );
      });
      if (!books) {
        localStorage.setItem("books", JSON.stringify(idItems));
        localStorage.setItem("stars", 0);
      }
      countStar();
    }
  });
});

fav = id => {
  const data = JSON.parse(localStorage.getItem("books"));
  let star = $(`#${id}`)[0].lastElementChild.firstElementChild;
  if (star.className.search("fas") === -1)
    star.className = star.className.replace("far", "fas");
  else star.className = star.className.replace("fas", "far");

  data[id] = !data[id];
  localStorage.setItem("books", JSON.stringify(data));
  countStar()
};

countStar = () => {
  const data = JSON.parse(localStorage.getItem("books"));
  let sumStar = 0;
  Object.values(data).forEach(value => {
    if (value) sumStar++;
  });
  localStorage.setItem("stars", sumStar);
  $('#star-count').text(sumStar);
};
