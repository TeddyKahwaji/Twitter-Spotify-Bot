const { rejects } = require("assert");
const dotenv = require("dotenv");
const { resolve } = require("path");
const Twitter = require("twitter");

let sinceId = "";
dotenv.config({ path: "./config.env" });

const twitterClient = new Twitter({
  consumer_key: process.env.API_KEY,
  consumer_secret: process.env.API_SECRET_KEY,
  access_token_key: process.env.ACCESS_TOKEN,
  access_token_secret: process.env.ACCESS_TOKEN_SECRET,
});

const getMentionedTweets = (sinceId) => {
  let params = sinceId == "" ? {} : { since_id: sinceId };

  console.log("--GETTING MENTIONED TWEETS FOR KAHWAJI08--");
  return new Promise((res, rej) => {
    twitterClient.get("statuses/mentions_timeline", params, (err, tweets) => {
      if (!err) {
        return res(tweets);
      } else {
        return rej(err);
      }
    });
  });
};

const Main = async () => {
  try {
    console.log(`RETRIEVING TWEET MENTIONS SINCE: ${sinceId}`);
    const mentions = await getMentionedTweets(sinceId);
    if (mentions.length !== 0) {
      let responses = [];
      for (let mention of mentions) {
        responses.push(mention.text);
      }
      let wordSegments = responses.join("").split(" ");
      sinceId = mentions[mentions.length - 1].id;
    } else {
      console.log("0 Mentions exist!");
    }
  } catch (e) {
    console.error(e);
  }
};

console.log("TWITTER BOT STARTED");
setInterval(Main, 10000);
