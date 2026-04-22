def style_transfer(content, style): return blend(content, style)
def style_transfer(content, style): return blend(content, style)
def style_transfer(content, style): return blend(content, style)
def style_transfer(content, style): return blend(content, style)
def style_transfer(content, style): return blend(content, style)
def style_transfer(content, style): return blend(content, style)
def style_transfer(content, style, strength=0.8): return blend(content, style, strength)
def style_transfer(content, style, strength=0.8): return blend(content, style, strength)

def compute_loss(content_features, style_features, generated_features, alpha=1.0, beta=1000.0):
    """Computes total loss as weighted sum of content and style loss."""
    content_loss = alpha * sum((cf - gf).pow(2).mean() for cf, gf in zip(content_features, generated_features))
    style_loss = beta * sum((sf.gram() - gf.gram()).pow(2).mean() for sf, gf in zip(style_features, generated_features))
    return content_loss + style_loss
