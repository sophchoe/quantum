# Test the Transformer class
import torch
from models import Transformer


def test_transformer():
    # Define parameters
    num_encoder_layers = 6
    num_decoder_layers = 6
    embed_len = 64
    num_heads = 8
    seq_len = 20
    batch_size = 32
    vocab_size = 100
    dropout = 0.1
    device = 'cpu'

    # Create an instance of Transformer
    model = Transformer(num_encoder_layers, num_decoder_layers,
                        embed_len, num_heads, batch_size, vocab_size, dropout, device)

    # Create dummy input tensors
    src = torch.randint(0, vocab_size, (batch_size, seq_len))
    tgt = torch.randint(0, vocab_size, (batch_size, seq_len))

    # Forward pass
    output = model(src, tgt)

    # Check the output shape
    assert output.shape == (
        batch_size, seq_len, vocab_size), f"Expected output shape {(batch_size, seq_len, vocab_size)}, but got {output.shape}"

    # Check the output type
    assert isinstance(
        output, torch.Tensor), f"Expected output type torch.Tensor, but got {type(output)}"

    print("Test passed!")
    return output.shape
