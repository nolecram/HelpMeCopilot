// get random quote from random API
const getQuote = async () => {
    const response = await fetch('https://api.quotable.io/random');
    const data = await response.json();
    return data;
    }
    // determine if the text is positive or negative
    const getSentiment = async (text) => {
    const response = await fetch('https://api.meaningcloud.com/sentiment-2.1?key=API_KEY&lang=en&txt=' + text);
    const data = await response.json();
    return data;
    }
    // get quote and sentiment
    const getQuoteAndSentiment = async () => {
    const quote = await getQuote();
    const sentiment = await getSentiment(quote.content);
    return { quote, sentiment };
    }
