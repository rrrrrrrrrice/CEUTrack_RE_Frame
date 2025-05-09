export CUDA_VISIBLE_DEVICES=6
export PYTHONWARNINGS=ignore::UserWarning
python /rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/tracking/train.py --script ceutrack --config ceutrack_fe108  \
 --save_dir ./output --mode multiple --nproc_per_node 1 --use_wandb  0