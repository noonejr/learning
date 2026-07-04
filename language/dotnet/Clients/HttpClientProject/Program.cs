using HttpClientProject.HttpClients.GameOfThrones;
using System;
using Microsoft.Extensions.Hosting;
using Microsoft.Extensions.DependencyInjection;

namespace HttpClientProject
{
    public class Program
    {
        public static async Task Main(string[] args)
        {
            var host = CreateHostBuilder(args).Build();

            var gameOfThronesHttpClient = host.Services.GetRequiredService<GameOfThronesHttpClient>();
            await gameOfThronesHttpClient.GetBooksAsync();
        }

        public static IHostBuilder CreateHostBuilder(string[] args) =>
            Host.CreateDefaultBuilder(args)
                .ConfigureServices((hostContext, services) =>
                {
                    services.AddHttpClient<GameOfThronesHttpClient>("gameOfThrones", (serviceProvider, client) =>
                    {
                        client.BaseAddress = new Uri("https://www.anapioficeandfire.com/api/");
                    });
                });
    }
}