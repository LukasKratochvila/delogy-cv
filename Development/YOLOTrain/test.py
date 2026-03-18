from ultralytics import YOLO

def test(yolo_model_folder, diff_testset):
    model = "runs/detect/trained/" + yolo_model_folder + "/weights/best.pt"
    test_data = "test_diff.yaml" if diff_testset else "test.yaml"
    root = "runs/detect/test_diff/" if diff_testset else "runs/detect/test/"

    metrics = YOLO(model).val(
        data = test_data,
        split = "test",
        batch = 32,
        workers = 0,
        device = 0,
        verbose = True,
        project = root,
        name = yolo_model_folder,
    )

    return metrics

def test_batch(batch, diff):
    folder1 = "real_real_" + batch
    folder2 = "real_generated_" + batch
    folder3 = "generated_real_" + batch
    folder4 = "generated_generated_" + batch

    test(folder1, diff)
    test(folder2, diff)
    test(folder3, diff)
    test(folder4, diff)


test("real_real_randaugment_x", True)
test("real_real_randaugment_x", False)