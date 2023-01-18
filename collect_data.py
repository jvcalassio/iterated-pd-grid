from mesa.batchrunner import batch_run
from datetime import datetime
import numpy as np
import pandas as pd
import os

from pd_grid.model import PdGrid

if __name__ == "__main__":
  params = {
    "width": 50,
    "height": 50,
    "schedule_type": 2, # Simultaneous
    "initial_cooperation": 0.5,
    "defection_award": list(np.arange(0,5.0,0.1))
  }

  iterations = 15
  max_steps = 200

  batch_results = batch_run(
    PdGrid,
    parameters=params,
    iterations=iterations,
    max_steps=max_steps,
    number_processes=6,
    # data_collection_period=1,
    display_progress=True
  )

  df = pd.DataFrame(batch_results)

  if not os.path.isdir("results"):
    os.makedirs("results")

  df.to_csv(f"results/results_{datetime.now().strftime('%d%m%Y-%H%M%S')}.csv")