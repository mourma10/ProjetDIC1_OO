from interface.root import *


def __main__():
    rootdim = CreateRootDimension()
    rootdim.popup_dim.mainloop()
    (dimx, dimy) = rootdim.getrootdimension()
    root_init = Tk()
    main_root = GetRoot(root_init, dimx, dimy)
    main_root.presentation()
    main_root.navigation()
    main_root.root.mainloop()


if __name__ == "__main__":
    __main__()
