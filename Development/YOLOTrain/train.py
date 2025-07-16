from ultralytics import YOLO

def train(train_data, augment, model_type):
    model = YOLO("yolo11" + model_type + ".pt")
    root = "runs/detect/trained"

    model.train(
        data = train_data + ".yaml",
        imgsz = 640,
        batch = 16,
        epochs = 100,
        workers = 0,
        device = 0,
        cache = True,
        auto_augment = augment, #(randaugment, autoaugment, augmix, None)

        project = root,
        name = train_data + "_" + augment + "_" + model_type,
    )

def train_custom(train_data):
    model = YOLO("yolo11m.pt")
    root = "runs/detect/trained"

    model.train(
        data = train_data + ".yaml",
        imgsz = 640,
        batch = 32,
        epochs = 100,
        workers = 0,
        device = 0,
        cache = True,

        auto_augment = None,
        degrees=10,
        translate=0.1,
        scale=0.1,
        shear=2.0,
        perspective=0.0005,
        flipud=0.2,
        fliplr=0.5,
        mosaic=1.0,
        mixup=0.1,
        hsv_h=0.015,
        hsv_s=0.7,
        hsv_v=0.4,

        project = root,
        name = train_data + "_custom",
    )


train("real_real", "randaugment", "x")