import tkinter as tk


class AssetStore:
    folder_img = """
    #define folder_width 16
    #define folder_height 16
    static unsigned char folder_bits[] = {
    0x00, 0x00, 0x3f, 0x00, 0xf1, 0x7f, 0x01, 0x40, 0xfd, 0xff, 0x07, 0x80,
    0x03, 0x80, 0x03, 0x80, 0x03, 0x80, 0x03, 0x80, 0x01, 0xc0, 0x01, 0x40,
    0x01, 0x40, 0x01, 0x40, 0xfe, 0x7f, 0x00, 0x00 };
    """
    folder_mask = """
    #define textfile_mask_width 16
    #define textfile_mask_height 16
    static unsigned char textfile_mask_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x06, 0x48, 0x06, 0x50, 0xf6, 0x67, 0x06, 0x60,
    0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40,
    0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0xfc, 0x3f };
    """

    image_img = """
    #define imagefile_width 16
    #define imagefile_height 16
    static unsigned char imagefile_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x22, 0x4c, 0x72, 0x52,
    0xfa, 0x52, 0x02, 0x4c, 0x02, 0x40, 0xfa, 0x40, 0x8a, 0x40, 0xfa, 0x40,
    0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };
    """
    image_mask = """
    #define imagefile_mask_width 16
    #define imagefile_mask_height 16
    static unsigned char imagefile_mask_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x3f, 0x02, 0x40, 0x22, 0x4c, 0x72, 0x52,
    0xfa, 0x52, 0x02, 0x4c, 0x02, 0x40, 0xfa, 0x40, 0x8a, 0x40, 0xfa, 0x40,
    0x02, 0x40, 0xfc, 0x3f, 0x00, 0x00, 0x00, 0x00 };
    """

    text_img = """
    #define textfile_width 16
    #define textfile_height 16
    static unsigned char textfile_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x06, 0x48, 0x06, 0x50, 0xf6, 0x67, 0x06, 0x60,
    0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40,
    0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0xfc, 0x3f };
    """
    text_mask = """
    #define textfile_mask_width 16
    #define textfile_mask_height 16
    static unsigned char textfile_mask_bits[] = {
    0x00, 0x00, 0xfc, 0x3f, 0x06, 0x48, 0x06, 0x50, 0xf6, 0x67, 0x06, 0x60,
    0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40,
    0x06, 0x40, 0xe6, 0x4f, 0x06, 0x40, 0xfc, 0x3f };
    """

    music_img = """
    #define musicfile_width 16
    #define musicfile_height 16
    static unsigned char musicfile_bits[] = {
    0x00, 0x1e, 0x00, 0x19, 0xc0, 0x16, 0x30, 0x11, 0xd0, 0x10, 0x30, 0x10,
    0x10, 0x10, 0x10, 0x10, 0x10, 0x0e, 0x10, 0x1f, 0x10, 0x1f, 0x0e, 0x1f,
    0x1f, 0x0e, 0x1f, 0x00, 0x1f, 0x00, 0x0e, 0x00 };
    """
    music_mask = """
    #define musicfile_mask_width 16
    #define musicfile_mask_height 16
    static unsigned char musicfile_mask_bits[] = {
    0x00, 0x1e, 0x00, 0x19, 0xc0, 0x16, 0x30, 0x11, 0xd0, 0x10, 0x30, 0x10,
    0x10, 0x10, 0x10, 0x10, 0x10, 0x0e, 0x10, 0x1f, 0x10, 0x1f, 0x0e, 0x1f,
    0x1f, 0x0e, 0x1f, 0x00, 0x1f, 0x00, 0x0e, 0x00 };
    """

    movie_img = """
    #define moviefile_width 16
    #define moviefile_height 16
    static unsigned char moviefile_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x7f, 0x02, 0x80, 0x0a, 0xb6, 0x1a, 0xb6,
    0x3a, 0xb6, 0x7a, 0xb6, 0x3a, 0xb6, 0x1a, 0xb6, 0x0a, 0xb6, 0x02, 0x80,
    0xfc, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
    """
    movie_mask = """
    #define moviefile_mask_width 16
    #define moviefile_mask_height 16
    static unsigned char moviefile_mask_bits[] = {
    0x00, 0x00, 0x00, 0x00, 0xfc, 0x7f, 0x02, 0x80, 0x0a, 0xb6, 0x1a, 0xb6,
    0x3a, 0xb6, 0x7a, 0xb6, 0x3a, 0xb6, 0x1a, 0xb6, 0x0a, 0xb6, 0x02, 0x80,
    0xfc, 0x7f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00 };
    """

    @classmethod
    def get_icon_by_extension(cls, extension):
        if isinstance(extension, str):
            extension = extension.lower()
        if extension is None or extension == "folder":
            return cls.folder()
        elif extension in ("png", "jpg", "image"):
            return cls.image()
        elif extension in ("webm", "mp4", "avi", "movie"):
            return cls.movie()
        elif extension in ("mp3", "wav", "music"):
            return cls.music()
        else:
            return cls.text()

    @classmethod
    def folder(cls):
        return tk.BitmapImage(data=cls.folder_img, maskdata=cls.folder_mask)

    @classmethod
    def image(cls):
        return tk.BitmapImage(data=cls.image_img, maskdata=cls.image_mask)

    @classmethod
    def movie(cls):
        return tk.BitmapImage(data=cls.movie_img, maskdata=cls.movie_mask)

    @classmethod
    def music(cls):
        return tk.BitmapImage(data=cls.music_img, maskdata=cls.music_mask)

    @classmethod
    def text(cls):
        return tk.BitmapImage(data=cls.text_img, maskdata=cls.text_mask)
