import pandas as pd

class Importable:
  @staticmethod
  def event():
    pass

  @staticmethod
  def ender(wf_module, table):
    if table is None:
      return None     # no rows to process

    col = wf_module.get_param('column').strip()
    value = float(wf_module.get_parm('value'))

    colnames = list(table.columns)
    if col in colnames:
        newtab = table[table[col]>value]

    return newtab


