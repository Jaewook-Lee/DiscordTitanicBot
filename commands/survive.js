const { SlashCommandBuilder, IntegrationApplication, InteractionCollector } = require('discord.js');
const onnx = require('onnxjs');    // I need this for running my onnx model in here.

/*
  Getting inputs from user. Inputs contain 'ticket fare', 'seat class', 'sex', and number of parents(or childs).
  Then we make these inputs to an onnx.Tensor for running onnx model in here.
  After then, we can run our model for getting result if user can survive at titanic or not.
*/
module.exports = {
    data: new SlashCommandBuilder()
        .setName('survive')
        .setDescription(`Let's predict if you can survive or not in the sinking of the Titanic!`)
        .addSubcommand(subcommand => 
            subcommand
                .setName('help')
                .setDescription(`Giving an example about how to type your informations.`)
          )
        .addSubcommand(subcommand =>
            subcommand
                .setName('input')
                .setDescription(`Typing your data. Read 'help' first.`)
                .addStringOption(option => 
                    option
                        .setName('info')
                        .setDescription(`fare seat-class sex number-of-parents(or childs) number-of-siblings(or spouses) age.`)
                        .setRequired(true)
            )
        ),
    async execute(interaction) {
        if (interaction.options.getSubcommand() == "help") {
            // Guideline for enter information.
            await interaction.reply("This is an explanation about how to write your information.\nWe need 6 informations. When you write your information we want they are seperated by blank.\nFor example, 14.3(ticket fare) 1(seat class) 0(sex, 0/1 = M/F) 0(number of parents(or childs)) 0(number of siblings(or spouses)) 20(age)");
        } else if (interaction.options.getSubcommand() == "input") {
            const information = interaction.options.getString('info');    // Get a string user entered.

            // Make an onnx session to running my onnx model.
            const sess = new onnx.InferenceSession();
            await sess.loadModel('./onnx_model.onnx');

            // Convert user's input to an array used for making an onnx.Tensor
            const inputArray = new Float32Array(information.split(' '));
            const userInput = new onnx.Tensor(inputArray, 'float32', [1, 6]);

            // Running my model, and getting result.
            const output = await sess.run([userInput]);
            const outputTensor = output.values().next().value;
            const result = outputTensor.data > 0.5;    // We promised if result value is over 0.5, survived!

            if (result) {
                interaction.reply('Congratulation! You survived from the Titanic!');
            } else {
                interaction.reply('Oops.. You died... RIP..');
            }
        }
    }
};