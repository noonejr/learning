using System;
using System.Net.Http;

namespace HttpClientProject.HttpClients.GameOfThrones
{
    /// <summary>
    /// Games Of Thrones HttpClient
    /// </summary>
    /// <see href="https://www.milanjovanovic.tech/blog/the-right-way-to-use-httpclient-in-dotnet">Implementation reference</see>
    public class GameOfThronesHttpClient
    {
        private const string baseUri = "https://www.anapioficeandfire.com/api/";

        private readonly HttpClient _client;

        /// <summary>
        /// Initializes a new instance of the <see cref="GameOfThronesHttpClient"/> class.
        /// </summary>
        /// <param name="client"></param>
        public GameOfThronesHttpClient(HttpClient client)
        {
            _client = client ?? throw new ArgumentNullException(nameof(client));
        }

        /// <summary>
        /// Gets all the game of thrones books
        /// </summary>
        /// <returns></returns>
        public async Task<string?> GetBooksAsync()
        {
            return await _client.GetStringAsync("books");
        }
    }
}