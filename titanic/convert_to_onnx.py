import torch

from dnn import DNN


if __name__ == '__main__':
    """
    This script converts a pytorch model(ends '.pt') to onnx model(ends '.onnx)
    Onnx model can run at JS.
    """
    pytorch_model = DNN()
    pytorch_model.load_state_dict(torch.load('custom_dnn.pt'))
    pytorch_model.eval()
    dummy_input = torch.ones((1, 6))

    # if verbose == true, print out string representation of graph.
    torch.onnx.export(pytorch_model, dummy_input, '../onnx_model.onnx', verbose=True)