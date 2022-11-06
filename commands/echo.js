const { SlashCommandBuilder } = require('discord.js');

/*
  Simple command
  Just echoing user's input.
*/
module.exports = {
    data: new SlashCommandBuilder().setName('echo').setDescription('Replies with your input!')
          .addStringOption(option => 
            option.setName('input').setDescription('The input to echo back').setRequired(true)),
    async execute(interaction) {
        const input = interaction.options.getString('input');
        await interaction.reply(input);
    }
};