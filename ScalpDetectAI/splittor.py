import os
import shutil
import random

def split_dataset(source_dir, train_dir, val_dir, test_dir, val_split=0.1, test_split=0.1):
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(val_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if not os.path.isdir(class_path):
            continue

        images = os.listdir(class_path)
        random.shuffle(images)

        val_size = int(len(images) * val_split)
        test_size = int(len(images) * test_split)
        train_size = len(images) - val_size - test_size

        splits = {
            train_dir: images[:train_size],
            val_dir: images[train_size:train_size + val_size],
            test_dir: images[train_size + val_size:]
        }

        for split_dir, image_list in splits.items():
            class_split_path = os.path.join(split_dir, class_name)
            os.makedirs(class_split_path, exist_ok=True)
            for img in image_list:
                src = os.path.join(class_path, img)
                dst = os.path.join(class_split_path, img)
                shutil.copyfile(src, dst)

# Example usage
source = r"C:\Users\Abubakar\Disease-detect\ScalpDetectAI\hairdiseasedataset\all"
split_dataset(
    source_dir=source,
    train_dir=r"C:\Users\Abubakar\Disease-detect\ScalpDetectAI\hairdiseasedataset\train",
    val_dir=r"C:\Users\Abubakar\Disease-detect\ScalpDetectAI\hairdiseasedataset\val",
    test_dir=r"C:\Users\Abubakar\Disease-detect\ScalpDetectAI\hairdiseasedataset\test"
)
