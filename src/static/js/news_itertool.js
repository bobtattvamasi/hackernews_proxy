// news_itertool.js


// Assuming you have an array of news items with the required fields
var newsItems = [
  {
    id: 36067464,
    rank: 27,
    title: 'How Life (and Death) Spring from Disorder (2017)',
    url: 'https://www.quantamagazine.org/how-life-and-death-spring-from-disorder-20170126/',
    site: 'quantamagazine.org',
    score: 15,
    user: 'yamrzou',
    timestamp: '2023-05-25T05:54:30',
    commentCount: 1
  },
  // Add more news items as needed
];

// Function to generate the HTML code for a single news item
function generateNewsItemHTML(item) {
  return `
    <tr class="spacer" style="height: 5px"></tr>
    <tr class="athing" id="${item.id}">
      <td align="right" valign="top" class="title">
        <span class="rank">${item.rank}.</span>
      </td>
      <td valign="top" class="votelinks">
        <center>
          <a id="up_${item.id}" href="http://127.0.0.1:8232/vote?id=${item.id}&amp;how=up&amp;goto=news">
            <div class="votearrow" title="upvote"></div>
          </a>
        </center>
      </td>
      <td class="title">
        <span class="titleline">
          <a href="${item.url}">${item.title}</a>
          <span class="sitebit comhead">
            (<a href="http://127.0.0.1:8232/from?site=${item.site}">
              <span class="sitestr">${item.site}</span>
            </a>)
          </span>
        </span>
      </td>
    </tr>
    <tr>
      <td colspan="2"></td>
      <td class="subtext">
        <span class="subline">
          <span class="score" id="score_${item.id}">${item.score} points</span>
          by <a href="http://127.0.0.1:8232/user?id=${item.user}" class="hnuser">${item.user}</a>
          <span class="age" title="${item.timestamp}">
            <a href="http://127.0.0.1:8232/item?id=${item.id}">4 hours ago</a>
          </span>
          <span id="unv_${item.id}"></span> |
          <a href="http://127.0.0.1:8232/hide?id=${item.id}&amp;goto=news">hide</a> |
          <a href="http://127.0.0.1:8232/item?id=${item.id}">${item.commentCount}&nbsp;comment</a>
        </span>
      </td>
    </tr>
  `;
}

// Get the table body element where the news items will be added
var table = document.querySelector('#news-table-body');

if (table) {
table.querySelectorAll('tr').forEach((row) => {

      // Получаем ссылку на элемент-родитель, куда хотим вставить HTML
var parentElement = document.getElementById('parentElementId');

// Создаем новый элемент div
var newDiv = document.createElement('div');

// Устанавливаем innerHTML нового div в содержимое строки row.innerHTML
newDiv.innerHTML = row.innerHTML;

// Вставляем новый div в родительский элемент
parentElement.appendChild(newDiv);
}
    )};