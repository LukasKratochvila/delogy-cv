import torch
import torchvision

# An instance of your model.
model = torchvision.models.get_model("ssdlite320_mobilenet_v3_large", weights=None, weights_backbone=None, num_classes=91) #torchvision.models.resnet18()
checkpoint = torch.load("trainBezAugRealReal/model_390_best.pth", map_location="cpu", weights_only=False)
model.load_state_dict(checkpoint["model"])
model.eval()

# An example input you would normally provide to your model's forward() method.
example = torch.rand(1, 3, 320, 320) #torch.rand(1, 3, 224, 224)

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)


traced_script_module.save("ssd_mobienet_320x320.pt")
