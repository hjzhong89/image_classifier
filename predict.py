import argparse
import model
import display

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='CLI for using TensorFlow model trained on oxford_flower102 to '
                                                 'classify an image')
    parser.add_argument('image_path',
                        metavar='image_path',
                        type=str,
                        help='Path to the image to classify')
    parser.add_argument('model_path',
                        metavar='model_path',
                        type=str,
                        help='Path to the keras model')
    parser.add_argument('--top_k', '--K',
                        metavar='top_k',
                        type=int,
                        help='Option to return top K results. If no value is provided, defaults to 5',
                        default=5)
    parser.add_argument('--category_names', '--C',
                        metavar='category_names',
                        type=str,
                        help='Path to JSON file that maps labels to category names. '
                             'If no value is provided, defaults to ./label_map.json',
                        default='label_map.json')

    args = parser.parse_args()
    image_path = args.image_path
    model_path = args.model_path
    top_k = args.top_k
    category_names = args.category_names

    print('Predicting with parameters')
    print('image_path: %s' % image_path)
    print('model_path: %s' % model_path)
    print('top_k: %s' % top_k)
    print('category_names: %s' % category_names)

    probs, labels = model.predict(image_path, model_path, top_k)
    display.display_results(image_path, probs, labels, category_names)
