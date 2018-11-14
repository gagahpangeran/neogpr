$(document).ready(() => {
  $.ajax({
    url: "/api/books/",
    success: result => {
      // const books = localStorage.getItem("books");
      // const idItems = {};
      result.data.map((item, index) => {
        // if (!books) idItems[item.id] = true;
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
              <i class='far fa-star' onclick='fav("${item.id}")'></i>
            </td>
          </tr>`
        );
      });
      // console.log(idItems);
    }
  });
});

fav = id => {
  let huhu = document.getElementById(id);
  let star = huhu.lastElementChild.firstElementChild;
};
