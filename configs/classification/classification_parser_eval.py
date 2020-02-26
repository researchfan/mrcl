import configargparse


class Parser(configargparse.ArgParser):
    def __init__(self):
        super().__init__()
        self.add('-c', '--my-config', is_config_file=True, default="configs/regression/empty.ini",
                 help='config file path')
        #
        self.add('--epoch', type=int, help='epoch number', default=1)
        self.add('--tasks', type=int, help='meta batch size, namely task num', default=4)
        self.add('--capacity', type=int, help='meta batch size, namely task num', default=100)
        self.add('--meta_lr', type=float, nargs='+', help='meta-level outer learning rate', default=[1e-4])
        self.add('--gpus', type=int, help='meta-level outer learning rate', default=1)
        self.add('--plasticity_lr', nargs='+', type=float, help='meta-level outer learning rate',
                 default=[1e-4])
        self.add('--modulation_lr', nargs='+', type=float, help='meta-level outer learning rate',
                 default=[1e-4])
        self.add('--attention_lr', nargs='+', type=float, help='meta-level outer learning rate',
                 default=[1e-4])
        self.add('--context_lr', nargs='+', type=float, help='meta-level outer learning rate',
                 default=[1e-4])
        self.add('--update_lr', nargs='+', type=float, help='task-level inner update learning rate',
                 default=[0.003])
        self.add('--update_step', type=int, help='task-level inner update steps', default=10)
        self.add('--name', help='Name of experiment', default="oml_regression")
        self.add('--model', help='Name of model', default="maml")
        self.add('--model-path', help='Path to model', default=None)
        self.add("--second-order", action="store_true", default=True)
        self.add("--no-plasticity", action="store_true")
        self.add("--no-sigmoid", action="store_true")
        self.add("--neuro", action="store_true")
        self.add("--no-meta", action="store_true")
        self.add("--no-save", action="store_true")
        self.add("--no-adaptation", action="store_true")
        self.add("--sanity", action="store_true")
        self.add("--context-plasticity", action="store_true")
        self.add('--seed', nargs='+', help='Seed', default=[90], type=int)
        self.add('--frequency', nargs='+', help='Seed', default=[1], type=int)
        self.add('--rank', type=int, help='meta batch size, namely task num', default=0)
        self.add("--width", type=int, default=400)
        self.add('--dataset', help='Name of experiment', default="omniglot")
        self.add('--path', help='Path of the dataset', default="../")

        self.add('--schedule', type=int, nargs='+', default=[10, 50, 75, 100, 150, 200],
                               help='Decrease learning rate at these epochs.')

        self.add('--memory', type=int, help='epoch number', default=0)
        self.add('--scratch', action='store_true', default=False)
        self.add('--reset', action="store_true")
        self.add('--test', action="store_true")
        self.add("--iid", action="store_true")
        self.add("--runs", type=int, default=5)

