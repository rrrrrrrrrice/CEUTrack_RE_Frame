export CUDA_VISIBLE_DEVICES=6
export PYTHONWARNINGS=ignore::UserWarning
export PYTHONPATH=/rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision:$PYTHONPATH
python /rydata/chenqiang/LLM_Tracking/LLM_Tracking_first_vision/tracking/test.py \
ceutrack ceutrack_coesot --dataset fe108 --threads 1 --num_gpus 1


