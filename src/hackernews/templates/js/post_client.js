// JavaScript code for interacting with the server
class PostClient {
  constructor() {
    this.socket = new WebSocket('ws://localhost:8232/ws/posts/'); // Replace with your server URL
    this.socket.addEventListener('message', this.handleMessage.bind(this));
  }

  emitToServer(message) {
    this.socket.send(JSON.stringify({ event: 'client_message', data: message }));
  }

  onServerMessage(callback) {
    this.socket.addEventListener('message', callback);
  }

  handleMessage(event) {
    const message = JSON.parse(event.data);
    // Handle server messages here
  }
}

// Function to generate the links dynamically
function generateLinks() {
  const links = [
    { name: 'new', url: 'http://127.0.0.1:8232/newest' },
    { name: 'past', url: 'http://127.0.0.1:8232/front' },
    { name: 'comments', url: 'http://127.0.0.1:8232/newcomments' },
    { name: 'ask', url: 'http://127.0.0.1:8232/ask' },
    { name: 'show', url: 'http://127.0.0.1:8232/show' },
    { name: 'jobs', url: 'http://127.0.0.1:8232/jobs' },
    { name: 'submit', url: 'http://127.0.0.1:8232/submit' }
  ];

  const linksContainer = document.querySelector('.pagetop');
  links.forEach((link) => {
    const linkElement = document.createElement('a');
    linkElement.href = link.url;
    linkElement.textContent = link.name;
    linksContainer.appendChild(linkElement);

    const separatorElement = document.createTextNode(' | ');
    linksContainer.appendChild(separatorElement);
  });
}

// Function to generate the post items dynamically
function generatePosts(posts) {
  const tableBody = document.querySelector('tbody');
  posts.forEach((post) => {
    const postRow = document.createElement('tr');
    postRow.className = 'athing';

    const rankCell = document.createElement('td');
    rankCell.align = 'right';
    rankCell.valign = 'top';
    rankCell.className = 'title';
    rankCell.innerHTML = `<span class="rank">${post.rank}</span>`;
    postRow.appendChild(rankCell);

    const voteCell = document.createElement('td');
    voteCell.valign = 'top';
    voteCell.className = 'votelinks';
    voteCell.innerHTML = `
      <center>
        <a id="up_${post.id}" href="vote?id=${post.id}&amp;how=up&amp;goto=news">
          <div class="votearrow" title="upvote"></div>
        </a>
      </center>
    `;
    postRow.appendChild(voteCell);

    const titleCell = document.createElement('td');
    titleCell.className = 'title';
    titleCell.innerHTML = `
      <a href="${post.url}" class="storylink">${post.title}</a>
      <span class="sitebit comhead">
        (<a href="from?site=${post.domain}">${post.domain}</a>)
      </span>
    `;
    postRow.appendChild(titleCell);

    const subtextRow = document.createElement('tr');
    const subtextCell = document.createElement('td');
    subtextCell.colSpan = '2';
    subtextCell.className = 'subtext';
    subtextCell.innerHTML = `
      <span class="score" id="score_${post.id}">${post.score}</span> points by
      <a href="user?id=${post.user}">${post.user}</a>
      <span class="age">
        <a href="item?id=${post.id}">${post.time}</a>
      </span>
      | <a href="hide?id=${post.id}&amp;goto=news">hide</a>
      | <a href="item?id=${post.id}">${post.comments_count} comments</a>
    `;
    subtextRow.appendChild(subtextCell);

    tableBody.appendChild(postRow);
    tableBody.appendChild(subtextRow);
  });
}

// Usage example
const postClient = new PostClient();
postClient.onServerMessage((event) => {
  const message = JSON.parse(event.data);
  if (message.event === 'posts_update') {
    const posts = message.data;
    generatePosts(posts);
  }
});

// Generate links and initial posts
generateLinks();
generatePosts();