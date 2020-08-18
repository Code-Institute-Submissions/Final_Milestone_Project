from django import forms
from images.models import Image, Image_Data


class AddSellerImage(forms.ModelForm):
    class Meta:
        model = Image
        fields = (
            'img_title', 'img_taken', 'base_price',
            'image', 'tmnl_img', 'user_id',)

    def __init__(self, *args, **kwargs):
        """ add placeholders, set/remove labels, and set autofocus """
        super().__init__(*args, **kwargs)

        placeholders = {
            'img_title': 'Image title displayed on the site',
            'img_taken': 'Date the image was taken',
            'base_price': 'Price (€) to be charged for a 6in x 4in print',
            'image': 'Image preview file',
            'tmnl_img': 'Thumbnail image file',
            'user_id': '',
        }

        self.fields['img_title'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'image' and field != 'tmnl_img' and field != 'user_id':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
                self.fields[field].label = False
            elif field == 'image' and field == 'tmnl_img':
                self.fields[field].label = placeholders[field]
            else:
                pass
            self.fields[field].widget.attrs['class'] = ''


class AddSellerImageData(forms.ModelForm):
    class Meta:
        model = Image_Data
        fields = (
            'make', 'model', 'focal_length', 'aperture',
            'shutter_speed_sec', 'iso', 'country', 'city')

    def __init__(self, *args, **kwargs):
        """ add placeholders, set/remove labels """
        super().__init__(*args, **kwargs)
        placeholders = {
            'make': 'Make of camera',
            'model': 'Camera model',
            'focal_length': 'Focal length setting',
            'aperture': 'Aperture setting',
            'shutter_speed_sec': 'Shutter speed (seconds)',
            'iso': 'ISO setting',
            'country': 'Country image taken',
            'city': 'Location image taken',
        }

        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            self.fields[field].widget.attrs['class'] = ''
