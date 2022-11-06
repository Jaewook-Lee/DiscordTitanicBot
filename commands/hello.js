const { SlashCommandBuilder } = require("discord.js");

/*
  Simple command
  Just saying hello.
*/
module.exports = {
    data: new SlashCommandBuilder().setName('hello').setDescription('Saying hello.'),
    async execute(interaction) {
        await interaction.reply('Hello! How are you?');
    },
};