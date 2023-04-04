if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/azanhelpdesk/Dq-Tom-New.git /Dq-Tom-New
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Dq-Tom-New
fi
cd /Dq-Tom-New
pip3 install -U -r requirements.txt
echo "Starting Dq-Tom-New...."
python3 bot.py
