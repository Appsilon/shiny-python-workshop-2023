from shiny import Inputs, Outputs, Session, App, reactive, render, req, ui

app_ui = ui.page_fluid(
    ui.input_text("input_txt", "Enter text"),
    ui.output_text_verbatim("output_txt"),
)


def server(input, output, session):
    @render.text
    def output_txt():
        return input.input_txt()


app = App(app_ui, server)
